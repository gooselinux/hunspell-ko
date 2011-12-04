Name: hunspell-ko
Summary: Korean hunspell dictionaries
Version: 0.3.3
Release: 1%{?dist}
Source: http://spellcheck-ko.googlecode.com/files/hunspell-dict-ko-%{version}.tar.gz
Group: Applications/Text
URL: http://code.google.com/p/spellcheck-ko/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: MPLv1.1 or GPLv2 or LGPLv2
BuildArch: noarch
BuildRequires: python-lxml

Requires: hunspell

%description
Korean hunspell dictionaries.

%prep
%setup -q -n hunspell-dict-ko-%{version}

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ko.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ko_KR.aff
cp -p ko.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ko_KR.dic

#tests busted upstream
#%check
#make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README LICENSE LICENSE.GPL LICENSE.LGPL LICENSE.MPL
%{_datadir}/myspell/*

%changelog
* Sun Aug 30 2009 Caolan McNamara <caolanm@redhat.com> - 0.3.3-1
- latest version

* Sun Jul 26 2009 Caolan McNamara <caolanm@redhat.com> - 0.3.2-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.3.1-1
- latest version

* Mon Jun 22 2009 Caolan McNamara <caolanm@redhat.com> - 0.3.0-1
- latest version

* Wed Jun 17 2009 Caolan McNamara <caolanm@redhat.com> - 0.2.4-2
- build from source

* Mon Jun 15 2009 Caolan McNamara <caolanm@redhat.com> - 0.2.4-1
- initial version
